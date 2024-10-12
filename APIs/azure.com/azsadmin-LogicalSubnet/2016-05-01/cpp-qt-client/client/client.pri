QT += network

HEADERS += \
# Models
    $${PWD}/OAILogicalSubnet.h \
    $${PWD}/OAILogicalSubnetList.h \
    $${PWD}/OAILogicalSubnetModel.h \
# APIs
    $${PWD}/OAILogicalSubnetsApi.h \
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
    $${PWD}/OAILogicalSubnet.cpp \
    $${PWD}/OAILogicalSubnetList.cpp \
    $${PWD}/OAILogicalSubnetModel.cpp \
# APIs
    $${PWD}/OAILogicalSubnetsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
