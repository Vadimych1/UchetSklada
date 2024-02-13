import "package:flutter/material.dart";

class TablePage extends StatefulWidget {
  const TablePage({super.key, required this.labels, required this.values});

  final List<String> labels;
  final List<String> values;

  @override
  State<TablePage> createState() => _TablePageState();
}

class _TablePageState extends State<TablePage> {
  Widget createTable(List labels, List values) {
    List<TableRow> rows = [];

    List<TableCell> headerCells = [];
    for (var label in labels) {
      headerCells.add(
        TableCell(child: Text(label)),
      );
    }

    TableRow headerRow = TableRow(children: headerCells);

    rows.add(headerRow);

    for (var value in values) {
      TableRow row = TableRow();

      for (var label in labels) {
        row.children.add(TableCell(child: Text(value[label])));
      }

      rows.add(row);
    }

    return Table(
      children: rows,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
