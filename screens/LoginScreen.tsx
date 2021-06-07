import * as React from 'react';
import { useNavigation } from '@react-navigation/native';
import { StackHeaderLeftButtonProps } from '@react-navigation/stack';

import { StyleSheet, StatusBar, TextInput } from 'react-native';

import { Text, View } from '../components/Themed';
import MenuIcon from '../components/MenuIcon';
import { useEffect } from 'react';
import main from '../styles/main';
import { ScrollView } from 'react-native-gesture-handler';

export default function LoginScreen() {
  const navigation = useNavigation();

  useEffect(() => {
    navigation.setOptions({
      headerLeft: (props: StackHeaderLeftButtonProps) => (<MenuIcon/>)
    });
  });

  return (
    <View style={main.centered}>
      <Text>Username</Text>
      <TextInput style={ styles.inputField }></TextInput>
      <Text>Password</Text>

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
    height: 40,
    alignItems: 'center',
    width: 10,
  },
});