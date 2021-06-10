import * as React from 'react';
import { useNavigation } from '@react-navigation/native';
import { StackHeaderLeftButtonProps } from '@react-navigation/stack';

import { StyleSheet, StatusBar, TextInput } from 'react-native';

import { Text, View } from '../components/Themed';
import MenuIcon from '../components/MenuIcon';
import { useEffect } from 'react';
import main from '../styles/main';
import { ScrollView } from 'react-native-gesture-handler';

export default function RegisterScreen() {
  const navigation = useNavigation();

  useEffect(() => {
    navigation.setOptions({
      headerLeft: (props: StackHeaderLeftButtonProps) => (<MenuIcon/>)
    });
  });

  return (
    <View style={main.centered}>
      <Text>Pick a Username:</Text>
      <TextInput style={ styles.inputField }></TextInput>
      <Text>{"\n\n"}Choose a Password:</Text>
      <TextInput secureTextEntry={true} style={ styles.inputField }></TextInput>
      <Text>Re-enter Password:</Text>
      <TextInput secureTextEntry={true} style={ styles.inputField }></TextInput>
    </View>
  )
};

const styles = StyleSheet.create({
  scrollView: {
    backgroundColor: 'pink',
    marginHorizontal: 20,
  },
  inputField: {
    backgroundColor: 'white',
    height: 30,
    alignItems: 'center',
    width: 200,
  },
});