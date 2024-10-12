QT += network

HEADERS += \
# Models
    $${PWD}/OAISlbMuxInstance.h \
    $${PWD}/OAISlbMuxInstanceList.h \
    $${PWD}/OAISlbMuxInstanceModel.h \
# APIs
    $${PWD}/OAISlbMuxInstancesApi.h \
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
    $${PWD}/OAISlbMuxInstance.cpp \
    $${PWD}/OAISlbMuxInstanceList.cpp \
    $${PWD}/OAISlbMuxInstanceModel.cpp \
# APIs
    $${PWD}/OAISlbMuxInstancesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
