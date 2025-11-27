<!-- Übersetzen Sie mehrere Dateien gleichzeitig in Deutsch -->

# Advanced GraphQL access

## Additional GraphQL APIs

In addition to auto-generated find APIs, there are APIs which help fetch a node value from IIH Semantics via GraphQL. There is a way to also use those APIs for mutation and subscription.

### Query

There are two APIs available here:

- ``QueryVariable`` - to query single variable. This API takes three parameters: ``NamespaceUrl``, ``Indentifier`` and the ``IdentifierType``. These are in line with the ``NodeId`` of OPC UA except that the NamespaceIndex is represented with the actual namespaceUrl. Error is thrown if ``NodeId`` does not match or the value provided cannot be casted to the datatype of OPC UA Variable.
- ``QueryVariables`` - This is a plural version of QueryVariable. This accepts array of OPC UA ``NodeIds``. The namespaceUrl is used here instead of NamespaceIndex. Array of errors is returned if ``NodeId`` does not match or the value provided cannot be casted to the datatype of OPC UA Variable.

These queries are lightweight and resolve into data directly from OPC UA.

### Mutation

Similar to query, there are two mutation APIs as well which works on single or multiple ``NodeIds``.

- WriteVariable - Accepts single ``NodeId`` along with the value in `string` format. It is required to provide value always in string format, this value is then parsed on server and written to OPC UA server. The value written will also be written to underlying Device if mapping is done correctly.
- WriteVariables - Accepts array of ``NodeIds`` along with the string values. All values are correctly written. An error is thrown if the ``NodeId`` does not match or the value provided cannot be casted to the datatype of OPC UA Variable.

### Subscription

This is a special API available which works over WebSockets and the built-in mechanism of GraphQL Subscription supports subscribing on live values streaming directly out of OPC UA Aggregation server.

The subscription API takes a ``nodeId`` as the input and prepares a subscription for it on the OPC UA Server. Whenever the data of the subscribed value changes, a message is delivered via the WebSocket channel of the GraphQL subscription.

## Access GraphQL APIs from Postman

The "Query Data" page in Common Configurator currently does not support the above-mentioned APIs, but it is possible to access them via Postman. When the IED is accessible via the local network, we can authenticate Postman and access GraphQL from outside of the IED.

Proceed as follow:

1. Log in to the IED.

    As shown in the image, use the IED URL ``https://<IED_HOST>/device/edge/api/v1/login/direct`` and username/password to authenticate to the device.

2. After logging in, the response will be a `access_token` and `refreshToken`. We only need the `access_token`. The access token will be sent as a cookie with ``authToken`` as the name, as shown below. Make sure you select GraphQL as the request type when creating a new request on Postman.

3. On the "Schema" tab of the Postman request, we can refresh and fetch the latest documentation of GraphQL. This documentation contains all found queries as well as the additional static queries which are documented above.

    As shown in diagram above, the query tab shows available GraphQL APIs and how to use them. We can choose either ``queryVariable`` or ``writeVariable`` and call the after filling in the correct parameters.

To find the namespace URL of a ``nodeId``, we can use UAExpert.

## Access GraphQL APIs from Altair Client

It is also possible to use the Windows-based Altair client to access GraphQL. You can download Altair UI from its [official website](https://altairgraphql.dev/). It can be used in a similar way to Postman.

1. You still require Postman to send the login request and get `access_token`. This `access_token` can then be used as below on Altair UI tu set header.

2. Set the request handlers as shown below:

3. Once the configuration is done, refresh the documentation.  
All APIs should be accessible as below.

The same UI can also be used to test the ``OnSubscribeVariables`` endpoint. If all setting are made correctly and a correct ``nodeId`` is specified, the subscription should provide live values.
