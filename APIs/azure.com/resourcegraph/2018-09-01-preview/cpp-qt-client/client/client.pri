QT += network

HEADERS += \
# Models
    $${PWD}/OAIColumn.h \
    $${PWD}/OAIColumnDataType.h \
    $${PWD}/OAIDateTimeInterval.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIFacet.h \
    $${PWD}/OAIFacetError.h \
    $${PWD}/OAIFacetRequest.h \
    $${PWD}/OAIFacetRequestOptions.h \
    $${PWD}/OAIFacetResult.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIQueryRequest.h \
    $${PWD}/OAIQueryRequestOptions.h \
    $${PWD}/OAIQueryResponse.h \
    $${PWD}/OAIResourceChangeData.h \
    $${PWD}/OAIResourceChangeDetailsRequestParameters.h \
    $${PWD}/OAIResourceChangeList.h \
    $${PWD}/OAIResourceChangesRequestParameters.h \
    $${PWD}/OAIResourceSnapshotData.h \
    $${PWD}/OAITable.h \
# APIs
    $${PWD}/OAIChangesApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIResourcesApi.h \
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
    $${PWD}/OAIColumn.cpp \
    $${PWD}/OAIColumnDataType.cpp \
    $${PWD}/OAIDateTimeInterval.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIFacet.cpp \
    $${PWD}/OAIFacetError.cpp \
    $${PWD}/OAIFacetRequest.cpp \
    $${PWD}/OAIFacetRequestOptions.cpp \
    $${PWD}/OAIFacetResult.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIQueryRequest.cpp \
    $${PWD}/OAIQueryRequestOptions.cpp \
    $${PWD}/OAIQueryResponse.cpp \
    $${PWD}/OAIResourceChangeData.cpp \
    $${PWD}/OAIResourceChangeDetailsRequestParameters.cpp \
    $${PWD}/OAIResourceChangeList.cpp \
    $${PWD}/OAIResourceChangesRequestParameters.cpp \
    $${PWD}/OAIResourceSnapshotData.cpp \
    $${PWD}/OAITable.cpp \
# APIs
    $${PWD}/OAIChangesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIResourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
