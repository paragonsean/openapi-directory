

# Pack


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowableOverhang** | **BigDecimal** | The amount an item can overhang lower items that it is placed upon. The units are whatever units the box and item dimensions are given in. By convention, inches. |  [optional] |
|**boxTypeSets** | **List&lt;BoxTypeSet&gt;** | predefined box types to be used, separated by commas. Will be overridden by boxTypes. Acceptable values are &lt;ul&gt;&lt;li&gt;\&quot;fedex\&quot;--FedEx OneRate&lt;/li&gt;&lt;li&gt;\&quot;usps\&quot;--USPS Priority Flat Rate&lt;/li&gt;&lt;li&gt;\&quot;pallet\&quot;--full-, half-, and quarter-sized 48\&quot;x40\&quot; pallets. |  [optional] |
|**boxTypes** | [**List&lt;BoxType&gt;**](BoxType.md) | box type definitions for packing, will override boxTypeSets defined. |  [optional] |
|**cohortMax** | **Integer** | the maximum number of contiguous cohorts for a given item type within a single container. E.g., if you pack 40 chairs in a single container, a cohortMax of 2 could yield one (all 40 chairs in a single block if space is availabe) or two (say, 25 chairs in one corner and 15 in the other) contiguous cohorts. |  [optional] |
|**cohortPacking** | **Boolean** | if selected, will ensure that all like items will be packed together, in no more than [cohortMax] different groups within a single container. |  [optional] |
|**coordOrder** | **List&lt;Integer&gt;** | If placementStyle is set to \&quot;default\&quot;, coordOrder sets the placement priority of axes ascendingly. \&quot;0,1,2\&quot; would search for placement points along the Z(length,\&quot;2\&quot;), then Y(width,\&quot;1\&quot;), and finally X(height\&quot;0\&quot;). Keep in mind that in the default rendering the \&quot;up\&quot; direction is X and the other axes follow the right-hand rule. This is useful for different packing methods. E.g., Utilizing \&quot;2,0,1\&quot; would pack a shipping container first in the Y(width) direction, then in the X(height) direction, and finally in the Z(length) direction, replication a floor-to-ceiling, front-to-back loading method. |  [optional] |
|**corners** | **Boolean** | only pack items at valid corner points of other items (optimal) |  [optional] |
|**eye** | [**Point**](Point.md) | The x,y,z coordinates of the virtual eye looking at the package for visualization purposes. Default is isometric, \&quot;1,1,1\&quot;. To generate a side view, one could use \&quot;0.001,1.0,0.001\&quot;. |  [optional] |
|**imgSize** | **Integer** | width of rendered SVGs in pixels. |  [optional] |
|**includeImages** | **Boolean** | include inline images, default is always on |  [optional] |
|**includeScripts** | **Boolean** | include inline javascripts and styles for base template |  [optional] |
|**interlock** | **Boolean** | alternates layFlat orientation by layer, so as to create an interlocked placement pattern and improve item stability. |  [optional] |
|**itemSets** | [**List&lt;ItemSet&gt;**](ItemSet.md) | item set definitions if not creating random items. |  [optional] |
|**key** | **String** | issued API key. |  [optional] |
|**layFlat** | **Boolean** | aligns all items laying flat. If possible, it may create a \&quot;brick-laying\&quot; pattern to increase stability. |  [optional] |
|**maxSequenceDistance** | **Integer** | This is the maximum distance allowable between two sequence values of items packed in a common box. E.g., \&quot;Distance\&quot; for an item sequence composed of aisle/bin combinations of \&quot;0401\&quot; and \&quot;1228\&quot; has a sequence distance of \\|1228 - 401\\| &#x3D; 827 |  [optional] |
|**n** | **Integer** | number of random items to generate and the quantity of each if \&quot;random\&quot; is set to true. a value of 5 would create 5 different items with a quantity of 5 each, making the total item quantity equal to n&amp;sup2; |  [optional] |
|**packOrigin** | [**Point**](Point.md) | the x,y,z coordinates of an optional packing origin. A packing origin is used to create more balanced packing for situations where load needs to be considered. E.g., for a 40\&quot;x48\&quot; pallet, a packOrigin representing the middle of the pallet, \&quot;0,20,24\&quot;, would cause placement to minimize the distance of the packed items from the center of the pallet. |  [optional] |
|**placementStyle** | [**PlacementStyleEnum**](#PlacementStyleEnum) | How to place items. &#39;default&#39; will defer to coordOrder, &#39;corner&#39; minimizes distance to rear, bottom corner, &#39;wedge&#39; minimizes distance to middle of bottom, back edge, &#39;mound&#39; minimizes distance to center of carton bottom. |  [optional] |
|**random** | **Boolean** | create random items |  [optional] |
|**randomMaxDimension** | **Integer** | maximum item dimension along a single axis for randomly generated items. |  [optional] |
|**randomMaxWeight** | **Integer** | maximum item weight for randomly generated items. |  [optional] |
|**rules** | [**List&lt;Rule&gt;**](Rule.md) | Array of packing rules. |  [optional] |
|**seed** | **Boolean** | if random is selected, seed the random number generator to deterministically generate random items to pack. |  [optional] |
|**sequenceHeatMap** | **Boolean** | Colorize items solely by their sequence value, light when sequence is high, dark when it is low. Useful for indicating item bin location, weight, or other sequence property that may not be apparent from the default visualization. |  [optional] |
|**sequenceSort** | **Boolean** | Whether or not the items should be initially sorted by their sequence value instead of their volume. This is not always useful, as the default \&quot;biggest-first\&quot; volume sort is very effective for items, and constraining by maxSequenceDistance is applied regardless of this field. That said, for doing custom pre-sorts such as weight-based instead of volume based, this value should be set to true. |  [optional] |
|**template** | [**TemplateEnum**](#TemplateEnum) | template name for markup generation. |  [optional] |
|**usableSpace** | **BigDecimal** | estimate of percentage space in boxes that is usable, i.e., not packing material. |  [optional] |
|**zone** | **Integer** | &lt;b&gt;[experimental]&lt;/b&gt; the shipping zone in order to use basic zone-based price optimization. |  [optional] |



## Enum: PlacementStyleEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| CORNER | &quot;corner&quot; |
| WEDGE | &quot;wedge&quot; |
| MOUND | &quot;mound&quot; |
| ORB | &quot;orb&quot; |



## Enum: TemplateEnum

| Name | Value |
|---- | -----|
| DEMO_TMPL | &quot;demo.tmpl&quot; |
| SHIPAPP_TMPL | &quot;shipapp.tmpl&quot; |
| BOAT_TMPL | &quot;boat.tmpl&quot; |



