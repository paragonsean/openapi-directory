QT += network

HEADERS += \
# Models
    $${PWD}/OAIVariable.h \
    $${PWD}/OAIVariableCreateOrUpdateParameters.h \
    $${PWD}/OAIVariableCreateOrUpdateProperties.h \
    $${PWD}/OAIVariableListResult.h \
    $${PWD}/OAIVariableProperties.h \
    $${PWD}/OAIVariableUpdateParameters.h \
    $${PWD}/OAIVariableUpdateProperties.h \
    $${PWD}/OAIVariable_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAIVariableApi.h \
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
    $${PWD}/OAIVariable.cpp \
    $${PWD}/OAIVariableCreateOrUpdateParameters.cpp \
    $${PWD}/OAIVariableCreateOrUpdateProperties.cpp \
    $${PWD}/OAIVariableListResult.cpp \
    $${PWD}/OAIVariableProperties.cpp \
    $${PWD}/OAIVariableUpdateParameters.cpp \
    $${PWD}/OAIVariableUpdateProperties.cpp \
    $${PWD}/OAIVariable_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAIVariableApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
