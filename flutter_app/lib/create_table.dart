import "package:flutter/material.dart";
import "package:http/http.dart";

const SERVERADDR = "localhost:8000";

class CreateTablePage extends StatelessWidget {
  const CreateTablePage({super.key});

  @override
  Widget build(BuildContext context) {
    TextEditingController nameController = TextEditingController();
    TextEditingController idController = TextEditingController();
    TextEditingController descriptionController = TextEditingController();

    return Scaffold(
      body: Column(
        children: [
          SizedBox(
            width: MediaQuery.of(context).size.width,
          ),
          const BackButton(),
          const Text('Создание таблицы', style: TextStyle(fontSize: 30)),
          Container(
            width: 600,
            height: 187,
            margin: const EdgeInsets.only(top: 30, bottom: 30),
            child: Form(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  TextField(
                    controller: nameController,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Название',
                    ),
                  ),
                  TextField(
                    controller: idController,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'ID таблицы (например, "my_table")',
                    ),
                  ),
                  TextField(
                    controller: descriptionController,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Описание таблицы',
                    ),
                  ),
                ],
              ),
            ),
          ),

          // Submit button
          ElevatedButton(
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(
                  content: Text('Создание таблицы...'),
                ),
              );

              get(
                Uri.http(
                  SERVERADDR,
                  "/create_table",
                  {
                    "displayName": nameController.text,
                    "name": idController.text,
                    "description": descriptionController.text
                  },
                ),
              ).then(
                (r) {
                  ScaffoldMessenger.of(context).hideCurrentSnackBar();
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text('Таблица создана'),
                    ),
                  );
                  Navigator.of(context).pop();
                },
              );
            },
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all<Color>(Colors.black),
              foregroundColor: MaterialStateProperty.all<Color>(Colors.white),
            ),
            child: const Text('Создать'),
          ),
        ],
      ),
    );
  }
}
