QT += network

HEADERS += \
# Models
    $${PWD}/OAISourceControl.h \
    $${PWD}/OAISourceControlCreateOrUpdateParameters.h \
    $${PWD}/OAISourceControlCreateOrUpdateProperties.h \
    $${PWD}/OAISourceControlListResult.h \
    $${PWD}/OAISourceControlProperties.h \
    $${PWD}/OAISourceControlSecurityTokenProperties.h \
    $${PWD}/OAISourceControlUpdateParameters.h \
    $${PWD}/OAISourceControlUpdateProperties.h \
    $${PWD}/OAISourceControl_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAISourceControlApi.h \
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
    $${PWD}/OAISourceControl.cpp \
    $${PWD}/OAISourceControlCreateOrUpdateParameters.cpp \
    $${PWD}/OAISourceControlCreateOrUpdateProperties.cpp \
    $${PWD}/OAISourceControlListResult.cpp \
    $${PWD}/OAISourceControlProperties.cpp \
    $${PWD}/OAISourceControlSecurityTokenProperties.cpp \
    $${PWD}/OAISourceControlUpdateParameters.cpp \
    $${PWD}/OAISourceControlUpdateProperties.cpp \
    $${PWD}/OAISourceControl_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAISourceControlApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
