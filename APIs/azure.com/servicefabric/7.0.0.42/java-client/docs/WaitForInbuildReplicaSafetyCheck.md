

# WaitForInbuildReplicaSafetyCheck

Safety check that waits for the replica build operation to finish. This indicates that there is a replica that is going through the copy or is providing data for building another replica. Bring the node down will abort this copy operation which are typically expensive involving data movements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|



