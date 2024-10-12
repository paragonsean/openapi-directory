QT += network

HEADERS += \
# Models
    $${PWD}/OAIEmptyResponse.h \
    $${PWD}/OAIErrorProto.h \
    $${PWD}/OAIErrors.h \
    $${PWD}/OAIGroup.h \
    $${PWD}/OAIGroupContentDetails.h \
    $${PWD}/OAIGroupItem.h \
    $${PWD}/OAIGroupItemResource.h \
    $${PWD}/OAIGroupSnippet.h \
    $${PWD}/OAIListGroupItemsResponse.h \
    $${PWD}/OAIListGroupsResponse.h \
    $${PWD}/OAIQueryResponse.h \
    $${PWD}/OAIResultTableColumnHeader.h \
# APIs
    $${PWD}/OAIGroupItemsApi.h \
    $${PWD}/OAIGroupsApi.h \
    $${PWD}/OAIReportsApi.h \
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
    $${PWD}/OAIEmptyResponse.cpp \
    $${PWD}/OAIErrorProto.cpp \
    $${PWD}/OAIErrors.cpp \
    $${PWD}/OAIGroup.cpp \
    $${PWD}/OAIGroupContentDetails.cpp \
    $${PWD}/OAIGroupItem.cpp \
    $${PWD}/OAIGroupItemResource.cpp \
    $${PWD}/OAIGroupSnippet.cpp \
    $${PWD}/OAIListGroupItemsResponse.cpp \
    $${PWD}/OAIListGroupsResponse.cpp \
    $${PWD}/OAIQueryResponse.cpp \
    $${PWD}/OAIResultTableColumnHeader.cpp \
# APIs
    $${PWD}/OAIGroupItemsApi.cpp \
    $${PWD}/OAIGroupsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
