QT += network

HEADERS += \
# Models
    $${PWD}/OAIBatchCreateRowsRequest.h \
    $${PWD}/OAIBatchCreateRowsResponse.h \
    $${PWD}/OAIBatchDeleteRowsRequest.h \
    $${PWD}/OAIBatchUpdateRowsRequest.h \
    $${PWD}/OAIBatchUpdateRowsResponse.h \
    $${PWD}/OAIColumnDescription.h \
    $${PWD}/OAICreateRowRequest.h \
    $${PWD}/OAIDateDetails.h \
    $${PWD}/OAILabeledItem.h \
    $${PWD}/OAIListRowsResponse.h \
    $${PWD}/OAIListTablesResponse.h \
    $${PWD}/OAIListWorkspacesResponse.h \
    $${PWD}/OAILookupDetails.h \
    $${PWD}/OAIRelationshipDetails.h \
    $${PWD}/OAIRow.h \
    $${PWD}/OAISavedView.h \
    $${PWD}/OAITable.h \
    $${PWD}/OAIUpdateRowRequest.h \
    $${PWD}/OAIWorkspace.h \
# APIs
    $${PWD}/OAITablesApi.h \
    $${PWD}/OAIWorkspacesApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIBatchCreateRowsRequest.cpp \
    $${PWD}/OAIBatchCreateRowsResponse.cpp \
    $${PWD}/OAIBatchDeleteRowsRequest.cpp \
    $${PWD}/OAIBatchUpdateRowsRequest.cpp \
    $${PWD}/OAIBatchUpdateRowsResponse.cpp \
    $${PWD}/OAIColumnDescription.cpp \
    $${PWD}/OAICreateRowRequest.cpp \
    $${PWD}/OAIDateDetails.cpp \
    $${PWD}/OAILabeledItem.cpp \
    $${PWD}/OAIListRowsResponse.cpp \
    $${PWD}/OAIListTablesResponse.cpp \
    $${PWD}/OAIListWorkspacesResponse.cpp \
    $${PWD}/OAILookupDetails.cpp \
    $${PWD}/OAIRelationshipDetails.cpp \
    $${PWD}/OAIRow.cpp \
    $${PWD}/OAISavedView.cpp \
    $${PWD}/OAITable.cpp \
    $${PWD}/OAIUpdateRowRequest.cpp \
    $${PWD}/OAIWorkspace.cpp \
# APIs
    $${PWD}/OAITablesApi.cpp \
    $${PWD}/OAIWorkspacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
