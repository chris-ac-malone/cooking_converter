import { GestureResponderEvent } from "react-native";

export type RootStackParamList = {
  Root: undefined;
  NotFound: undefined;
};

export type BottomTabParamList = {
  TabOne: undefined;
  TabTwo: undefined;
};

export type TabOneParamList = {
  TabOneScreen: undefined;
};

export type DrawerParamList = {
  Profile: undefined;
  Settings: undefined;
  Home: undefined;  
  Login: undefined;
};

export type ProfileParamList = {
  ProfileScreen: undefined;
  LoginScreen: undefined;
  RegisterScreen: undefined;
};

export type SettingsParamList = {
  SettingsScreen: undefined;
};

export type HomeParamList = {
  HomeScreen: undefined;
};

export type LoginParamList = {
  LoginScreen: undefined;
};

export type onPressFunc = (event: GestureResponderEvent) => void;
