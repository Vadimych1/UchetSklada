import 'package:flutter/material.dart';
import 'create_table.dart';
import 'tables.dart';
import 'package:window_manager/window_manager.dart';
import 'package:http/http.dart';
import 'dart:convert';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await WindowManager.instance.ensureInitialized();
  windowManager.waitUntilReadyToShow().then(
    (_) async {
      await windowManager.setTitle('Складской менеджер');
    },
  );

  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<Widget> tableButtons = [];
  List<Widget> alerts = [];

  @override
  void initState() {
    super.initState();

    get(Uri.http("localhost:8000", "/get_tables")).then(
      (r) {
        if (r.statusCode == 200) {
          var tables = jsonDecode(r.body);

          for (var element in tables) {
            setState(
              () {
                tableButtons.add(
                  ElevatedButton(
                    style: ButtonStyle(
                      backgroundColor: MaterialStateProperty.all<Color>(
                        Colors.white,
                      ),
                      foregroundColor: MaterialStateProperty.all<Color>(
                        Colors.black,
                      ),
                    ),
                    onPressed: () {
                      // Open
                    },
                    child: Row(
                      children: [
                        Text(element["name"]),
                        IconButton(
                          onPressed: () {
                            // Delete
                            get(
                              Uri.http(
                                "localhost:8000",
                                "/delete_table",
                                {
                                  "name": element["name"],
                                },
                              ),
                            ).then(
                              (r) {
                                Navigator.of(context).pop();
                                Navigator.of(context).push(
                                  MaterialPageRoute(
                                    builder: (context) => const MyHomePage(),
                                  ),
                                );
                              },
                            );
                          },
                          icon: const Icon(Icons.delete),
                          color: Colors.red,
                        ),
                      ],
                    ),
                  ),
                );
              },
            );
          }
        }
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // footer
      bottomNavigationBar: const BottomAppBar(
        color: Colors.black,
        child: Row(
          children: [
            // OK state
            Icon(Icons.check, color: Colors.white),
            SizedBox(width: 10),
            Text('Сервер подключен', style: TextStyle(color: Colors.white)),
          ],
        ),
      ),
      body: Container(
        padding: const EdgeInsets.symmetric(horizontal: 20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Складской менеджер',
              style: TextStyle(fontSize: 30),
            ),

            // Tables buttons
            Container(
              margin: const EdgeInsets.only(top: 30, bottom: 30),
              width: MediaQuery.of(context).size.width,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.black,
                borderRadius: BorderRadius.circular(10),
              ),
              child: tableButtons.isNotEmpty
                  ? Row(children: tableButtons)
                  : const Text(
                      "Таблиц нет, создайте ниже",
                      style: TextStyle(color: Colors.white, fontSize: 20),
                    ),
            ),

            // Action buttons
            Container(
              margin: const EdgeInsets.only(bottom: 10),
              child: const Text(
                'Действия',
                style: TextStyle(fontSize: 20),
              ),
            ),

            Flex(
              direction: Axis.horizontal,
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              mainAxisSize: MainAxisSize.max,
              children: [
                // Add table
                ElevatedButton.icon(
                  onPressed: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => const CreateTablePage(),
                      ),
                    );
                  },
                  icon: const Icon(Icons.add),
                  label: const Text('Создать таблицу'),
                  style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all<Color>(Colors.black),
                    foregroundColor:
                        MaterialStateProperty.all<Color>(Colors.white),
                  ),
                ),
              ],
            ),

            // Alerts
            Container(
              margin: const EdgeInsets.only(bottom: 10, top: 20),
              child: const Text(
                'Уведомления',
                style: TextStyle(fontSize: 20),
              ),
            ),

            Container(
              child: Flex(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.center,
                direction: Axis.horizontal,
                children:
                    alerts.isEmpty ? [const Text('Нет уведомлений')] : alerts,
              ),
            ),

            // Add width
            SizedBox(
              width: MediaQuery.of(context).size.width,
            ),
          ],
        ),
      ),
    );
  }
}
