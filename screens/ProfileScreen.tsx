import * as React from 'react';
import { useNavigation } from '@react-navigation/native';
import { StackHeaderLeftButtonProps } from '@react-navigation/stack';
import { StyleSheet, StatusBar } from 'react-native';

import { Text, View } from '../components/Themed';
import MenuIcon from '../components/MenuIcon';
import { useEffect } from 'react';
import main from '../styles/main';
import { TouchableOpacity } from 'react-native-gesture-handler';


export default function ProfileScreen() {
  const navigation = useNavigation();
  const onPressLogin = () => navigation.navigate("LoginScreen");
  const onPressRegister = () => navigation.navigate("RegisterScreen");

  useEffect(() => {
    navigation.setOptions({
      showHeader: true,
      headerLeft: (props: StackHeaderLeftButtonProps) => (<MenuIcon/>)
    });
  });

  return (
    <View style={ styles.container }>
      <View style={ styles.textContainer }>
        <Text
          style={ styles.displayMessage }
          lightColor="rgba(0,0,0,0.8)"
          darkColor="rgba(255,255,255,0.8)"
        >
          You are not currently logged in:
        </Text>
      </View>
      <View style={ styles.buttonContainer }>
        <TouchableOpacity style={ styles.loginButton } onPress={ onPressLogin }>
          <Text style={ styles.loginButtonText }>Login</Text>
        </TouchableOpacity>
        <TouchableOpacity style={ styles.registerButton } onPress={ onPressRegister }>
          <Text style={ styles.registerButtonText }>Register</Text>
        </TouchableOpacity>
      </View>
    </View>
  )
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column",
  },
  textContainer: {
    flex: 3,
    justifyContent: "space-between",
    flexDirection: "column",
  },
  displayMessage: {
    textAlign: "center",
    justifyContent: "space-between",
    fontSize: 16,
    color: "#fff",
    paddingTop: "50%",
    flex: 1,
  },
  buttonContainer: {
    flexDirection: "row",
    justifyContent: "center",
    flexGrow: 1,
  },
  loginButton: {
    flex: 1,
    flexGrow: 1,
    justifyContent: "space-evenly",
    width: 150,
    backgroundColor: "#000",
  },
  registerButton: {
    flex: 1,
    flexGrow: 1,
    justifyContent: "space-evenly",
    width: 150,
    backgroundColor: "#000",
  },
  loginButtonText: {
    padding: 8,
    margin: 10,
    color: "#FFF",
    textAlign: "center",
    fontSize: 19,
  },
  registerButtonText: {
    padding: 8,
    margin: 10,
    color: "#FFF",
    textAlign: "center",
    fontSize: 19,
  }
})