# Connecting third-party apps to GraphQL

If you want to query data from GraphQL with user-developed applications, use the following connection information.

## Access within the app

* Endpoint for GraphQL queries: ``http://pdm-core-service:80/api/graphql``

* Websocket subscriptions: ``ws://pdm-core-service:80/api/graphql``

## Access outside the app

* Endpoint for GraphQL queries: ``https://<IED-IP/IED-DNS\>/iih-core-config/api/graphql``

* Websocket subscriptions: ``wss://<IED-IP/IED-DNS\>/iih-core-config/api/graphql``
