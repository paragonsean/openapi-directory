QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_details_inner.h \
    $${PWD}/OAILocationBasedServicesAccount.h \
    $${PWD}/OAILocationBasedServicesAccountCreateParameters.h \
    $${PWD}/OAILocationBasedServicesAccountKeys.h \
    $${PWD}/OAILocationBasedServicesAccountUpdateParameters.h \
    $${PWD}/OAILocationBasedServicesAccounts.h \
    $${PWD}/OAILocationBasedServicesAccountsMoveRequest.h \
    $${PWD}/OAILocationBasedServicesKeySpecification.h \
    $${PWD}/OAILocationBasedServicesOperations.h \
    $${PWD}/OAILocationBasedServicesOperations_value_inner.h \
    $${PWD}/OAILocationBasedServicesOperations_value_inner_display.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_details_inner.cpp \
    $${PWD}/OAILocationBasedServicesAccount.cpp \
    $${PWD}/OAILocationBasedServicesAccountCreateParameters.cpp \
    $${PWD}/OAILocationBasedServicesAccountKeys.cpp \
    $${PWD}/OAILocationBasedServicesAccountUpdateParameters.cpp \
    $${PWD}/OAILocationBasedServicesAccounts.cpp \
    $${PWD}/OAILocationBasedServicesAccountsMoveRequest.cpp \
    $${PWD}/OAILocationBasedServicesKeySpecification.cpp \
    $${PWD}/OAILocationBasedServicesOperations.cpp \
    $${PWD}/OAILocationBasedServicesOperations_value_inner.cpp \
    $${PWD}/OAILocationBasedServicesOperations_value_inner_display.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
