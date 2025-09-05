import 'package:flutter/material.dart';
import 'screens/home_screens.dart';

void main(){
  runApp(MemoryFlipChallenge());
}

class MemoryFlipChallenge extends StatelessWidget {
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: 'Memory Flip Challenge',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: HomeScreen(),
    );
  }
}