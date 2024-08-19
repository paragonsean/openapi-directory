QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvisor.h \
    $${PWD}/OAIAdvisorListResult.h \
    $${PWD}/OAIAdvisorProperties.h \
# APIs
    $${PWD}/OAIDatabaseAdvisorsApi.h \
    $${PWD}/OAIServerAdvisorsApi.h \
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
    $${PWD}/OAIAdvisor.cpp \
    $${PWD}/OAIAdvisorListResult.cpp \
    $${PWD}/OAIAdvisorProperties.cpp \
# APIs
    $${PWD}/OAIDatabaseAdvisorsApi.cpp \
    $${PWD}/OAIServerAdvisorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
