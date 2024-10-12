# ServiceFabricClientApis.ChaosTargetFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationInclusionList** | **[String]** | A list of application URI&#39;s to include in Chaos faults. All replicas belonging to services of these applications are amenable to replica faults (restart replica, remove replica, move primary, and move secondary) by Chaos. Chaos may restart a code package only if the code package hosts replicas of these applications only. If an application does not appear in this list, it can still be faulted in some Chaos iteration if the application ends up on a node of a node type that is included in NodeTypeInclusionList. However if applicationX is tied to nodeTypeY through placement constraints and applicationX is absent from ApplicationInclusionList and nodeTypeY is absent from NodeTypeInclusionList, then applicationX will never be faulted. At most 1000 application names can be included in this list, to increase this number, a config upgrade is required for MaxNumberOfApplicationsInChaosEntityFilter configuration.  | [optional] 
**nodeTypeInclusionList** | **[String]** | A list of node types to include in Chaos faults. All types of faults (restart node, restart code package, remove replica, restart replica, move primary, and move secondary) are enabled for the nodes of these node types. If a nodetype (say NodeTypeX) does not appear in the NodeTypeInclusionList, then node level faults (like NodeRestart) will never be enabled for the nodes of NodeTypeX, but code package and replica faults can still be enabled for NodeTypeX if an application in the ApplicationInclusionList. happens to reside on a node of NodeTypeX. At most 100 node type names can be included in this list, to increase this number, a config upgrade is required for MaxNumberOfNodeTypesInChaosEntityFilter configuration.  | [optional] 


