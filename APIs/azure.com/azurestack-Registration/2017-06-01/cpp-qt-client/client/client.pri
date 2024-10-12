QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivationKeyResult.h \
    $${PWD}/OAIRegistration.h \
    $${PWD}/OAIRegistrationList.h \
    $${PWD}/OAIRegistrationParameter.h \
    $${PWD}/OAIRegistrationParameterProperties.h \
    $${PWD}/OAIRegistrationProperties.h \
    $${PWD}/OAIRegistrations_List_default_response.h \
    $${PWD}/OAIRegistrations_List_default_response_error.h \
# APIs
    $${PWD}/OAIRegistrationsApi.h \
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
    $${PWD}/OAIActivationKeyResult.cpp \
    $${PWD}/OAIRegistration.cpp \
    $${PWD}/OAIRegistrationList.cpp \
    $${PWD}/OAIRegistrationParameter.cpp \
    $${PWD}/OAIRegistrationParameterProperties.cpp \
    $${PWD}/OAIRegistrationProperties.cpp \
    $${PWD}/OAIRegistrations_List_default_response.cpp \
    $${PWD}/OAIRegistrations_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIRegistrationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
