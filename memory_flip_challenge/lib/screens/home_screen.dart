import 'package:flutter/material.dart';
import 'game_screen.dart';

class HomeScreen extends StatelessWidget {
    @override
    Widget build(BuildContext context){
        return Scaffold(
            backgroundColor: Colors.deepPurple[50],
            body: Center(
                child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                        padding: EdgeInsets.symmetric(horizontal: 30, vertical: 15),
                        backgroundColor: Colors.deepPurple,
                    ),
                    onPressed: () {
                        Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => GameScreen()),
                        );
                    },
                    child: Text(
                        'Start Game',
                        style: TextStyle(fontSize: 24, color: Colors.white),
                    ),
                ),
            ),
        );
    }
}