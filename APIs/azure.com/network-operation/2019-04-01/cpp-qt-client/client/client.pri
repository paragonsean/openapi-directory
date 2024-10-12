QT += network

HEADERS += \
# Models
    $${PWD}/OAIAvailability.h \
    $${PWD}/OAIDimension.h \
    $${PWD}/OAILogSpecification.h \
    $${PWD}/OAIMetricSpecification.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperationPropertiesFormat.h \
    $${PWD}/OAIOperationPropertiesFormat_serviceSpecification.h \
    $${PWD}/OAIOperation_display.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAvailability.cpp \
    $${PWD}/OAIDimension.cpp \
    $${PWD}/OAILogSpecification.cpp \
    $${PWD}/OAIMetricSpecification.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperationPropertiesFormat.cpp \
    $${PWD}/OAIOperationPropertiesFormat_serviceSpecification.cpp \
    $${PWD}/OAIOperation_display.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
