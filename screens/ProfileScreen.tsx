import * as React from 'react';
import { useNavigation } from '@react-navigation/native';
import { StackHeaderLeftButtonProps } from '@react-navigation/stack';

import { Text, View } from '../components/Themed';
import MenuIcon from '../components/MenuIcon';
import { useEffect } from 'react';
import main from '../styles/main';
import { TouchableOpacity } from 'react-native-gesture-handler';


export default function ProfileScreen() {
  const navigation = useNavigation();
  const onPress = () => navigation.navigate("LoginScreen");

  useEffect(() => {
    navigation.setOptions({
      showHeader: true,
      headerLeft: (props: StackHeaderLeftButtonProps) => (<MenuIcon/>)
    });
  });

  return (
    <View style={main.centered}>
      <Text
        lightColor="rgba(0,0,0,0.8)"
        darkColor="rgba(255,255,255,0.8)"
      >
        Profile
      </Text>
      <TouchableOpacity onPress={ onPress }>
        <Text>Login</Text>
      </TouchableOpacity>
    </View>
  )
};
