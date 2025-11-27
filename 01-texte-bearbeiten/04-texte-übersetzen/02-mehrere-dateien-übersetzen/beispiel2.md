# Filtering data

## Hierarchical filtering of objects

The filtering approach follows the same general syntax as the object retrieval syntax. It is possible to filter by more than one object. The objects can have different basic data types, such as String, Numeric, Boolean. The filter can be applied only at the beginning of the object retrieval query and only to the top-level object. The list of top-level objects is filtered in this way.

Only the child object of top-level objects can be the first level of the filter; its child object in the hierarchy can be used in later levels.

You can also filter with create alternatives (and/or).

## Filter operators

Literal objects are the only ones to which a filter operator can be applied. The operator types available for each literal type vary. Below are the operator types of various data types:

* String<br/>
    * Equal to; eq
    * Contains
* Floating point numbers (float)/Numbers (integer)<br/>
    * Equal to; eq
    * Less than; lt
    * Greater than; gt
* Bool<br/>
    * Equal to; eq

Explanation:

* eq: The 'equal to' operator; searchItem = ProvidedValue
* contains: This is the 'Search' operator for substrings; the searchItem contains the substring ProvidedValue.
* lt: This is the 'less than' operator applied to numerical data types; searchItem < ProvidedValue
* gt: This is the 'greater than' operator applied to numerical data types; searchItem > ProvidedValue

## Filtering information in the Common Configurator

To filter the queries by particular information, proceed as follows:

1. Open the Common Configurator.
1. Open the query editor in the "Provide information" tab.
1. Double-click the "Query" object.
1. Search for the desired node and double-click the node(s) in each case in the query editor.<br/>
  The nodes are displayed in the tree view.
1. Move the cursor over the "Query" node and click on the icon Filter:<br/>
  In the settings, you can select the query type and set the filter for each child object:<br/>
1. Click on "Confirm".
