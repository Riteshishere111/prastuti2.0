import 'package: flutter/material.dart';

class GameScreen extends StatelesWidget {
    @overrideWidget build(BuildContext context) {
        return Scaffold(
            backgroundColor: Colors.deepPurple[50],
            appBar: AppBar(
                title: Text('Memory Flip Challenge'),
            ),
            body: Center(
                child: Text(
                    'Game Screen',
                    style: TextStyle(fontSize: 24),
                ),
            ),
        );
    }
}