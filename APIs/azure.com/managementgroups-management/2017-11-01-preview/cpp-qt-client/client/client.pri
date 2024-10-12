QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateManagementGroupRequest.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIManagementGroup.h \
    $${PWD}/OAIManagementGroupChildInfo.h \
    $${PWD}/OAIManagementGroupChildType.h \
    $${PWD}/OAIManagementGroupDetails.h \
    $${PWD}/OAIManagementGroupInfo.h \
    $${PWD}/OAIManagementGroupInfoProperties.h \
    $${PWD}/OAIManagementGroupListResult.h \
    $${PWD}/OAIManagementGroupProperties.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIParentGroupInfo.h \
# APIs
    $${PWD}/OAIManagementGroupsApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAICreateManagementGroupRequest.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIManagementGroup.cpp \
    $${PWD}/OAIManagementGroupChildInfo.cpp \
    $${PWD}/OAIManagementGroupChildType.cpp \
    $${PWD}/OAIManagementGroupDetails.cpp \
    $${PWD}/OAIManagementGroupInfo.cpp \
    $${PWD}/OAIManagementGroupInfoProperties.cpp \
    $${PWD}/OAIManagementGroupListResult.cpp \
    $${PWD}/OAIManagementGroupProperties.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIParentGroupInfo.cpp \
# APIs
    $${PWD}/OAIManagementGroupsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
