QT += network

HEADERS += \
# Models
    $${PWD}/OAIDashboard.h \
    $${PWD}/OAIDashboardLens.h \
    $${PWD}/OAIDashboardListResult.h \
    $${PWD}/OAIDashboardParts.h \
    $${PWD}/OAIDashboardParts_position.h \
    $${PWD}/OAIDashboardProperties.h \
    $${PWD}/OAIErrorDefinition.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPatchableDashboard.h \
    $${PWD}/OAIResourceProviderOperation.h \
    $${PWD}/OAIResourceProviderOperationList.h \
    $${PWD}/OAIResourceProviderOperation_display.h \
# APIs
    $${PWD}/OAIDashboardApi.h \
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
    $${PWD}/OAIDashboard.cpp \
    $${PWD}/OAIDashboardLens.cpp \
    $${PWD}/OAIDashboardListResult.cpp \
    $${PWD}/OAIDashboardParts.cpp \
    $${PWD}/OAIDashboardParts_position.cpp \
    $${PWD}/OAIDashboardProperties.cpp \
    $${PWD}/OAIErrorDefinition.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPatchableDashboard.cpp \
    $${PWD}/OAIResourceProviderOperation.cpp \
    $${PWD}/OAIResourceProviderOperationList.cpp \
    $${PWD}/OAIResourceProviderOperation_display.cpp \
# APIs
    $${PWD}/OAIDashboardApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
