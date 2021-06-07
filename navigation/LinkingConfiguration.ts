import * as Linking from 'expo-linking';

export default {
  prefixes: [Linking.makeUrl('/')],
  config: {
    screens: {
      Root: {
        screens: {
          Profile: {
            screens: {
              ProfileScreen: 'profile',
              LoginScreen: 'login'
            }
          },
          Settings: {
            screens: {
              SettingsScreen: 'settings'
            }
          },
          Clients: {
            screens: {
              ClientsScreen: 'clients'
            }
          }
        },
      },
      NotFound: '*',
    },
  },
};
