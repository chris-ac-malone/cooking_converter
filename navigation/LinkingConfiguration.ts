import * as Linking from 'expo-linking';

export default {
  prefixes: [Linking.makeUrl('/')],
  config: {
    screens: {
      Root: {
        screens: {
          Profile: {
            screens: {
              ProfileScreen: 'profile'
            }
          },
          Settings: {
            screens: {
              SettingsScreen: 'Settings'
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
