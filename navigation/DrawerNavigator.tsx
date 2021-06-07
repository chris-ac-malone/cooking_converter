import { createStackNavigator } from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import * as React from 'react';

import ProfileScreen from '../screens/ProfileScreen';
import SettingsScreen from '../screens/SettingsScreen';
import HomeScreen from '../screens/HomeScreen';
import LoginScreen from '../screens/LoginScreen';
import { DrawerParamList, ProfileParamList, SettingsParamList, HomeParamList, LoginParamList } from '../types';

const Drawer = createDrawerNavigator<DrawerParamList>();

export default function DrawerNavigator() {
  return (
    <Drawer.Navigator>
      <Drawer.Screen
        name="Profile"
        component={ProfileNavigator}/>
      <Drawer.Screen
        name="Settings"
        component={SettingsNavigator}
      />
      <Drawer.Screen
        name="Home"
        component={HomeNavigator}
      />
    </Drawer.Navigator>
  );
}

const ProfileStack = createStackNavigator<ProfileParamList>();

function ProfileNavigator() {
  return (
    <ProfileStack.Navigator>
      <ProfileStack.Screen
        name="ProfileScreen"
        component={ProfileScreen}
        options={{
          title: 'Profile',
        }}
      />
      <ProfileStack.Screen 
        name="LoginScreen"
        component={LoginScreen}
      />
    </ProfileStack.Navigator>
  )
}

const SettingsStack = createStackNavigator<SettingsParamList>();

function SettingsNavigator() {
  return (
    <SettingsStack.Navigator>
      <SettingsStack.Screen
        name="SettingsScreen"
        component={SettingsScreen}
        options={{
          title: 'Settings',
        }}
      />
    </SettingsStack.Navigator>
  )
}

const HomeStack = createStackNavigator<HomeParamList>();

function HomeNavigator() {
  return (
    <HomeStack.Navigator>
      <HomeStack.Screen
        name="HomeScreen"
        component={HomeScreen}
        options={{
          title: 'Your Feed',
        }}
      />
    </HomeStack.Navigator>
  )
}