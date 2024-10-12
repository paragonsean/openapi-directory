QT += network

HEADERS += \
# Models
    $${PWD}/OAIBastionHost.h \
    $${PWD}/OAIBastionHostIPConfiguration.h \
    $${PWD}/OAIBastionHostIPConfigurationPropertiesFormat.h \
    $${PWD}/OAIBastionHostIPConfigurationPropertiesFormat_publicIPAddress.h \
    $${PWD}/OAIBastionHostListResult.h \
    $${PWD}/OAIBastionHostPropertiesFormat.h \
# APIs
    $${PWD}/OAIBastionHostsApi.h \
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
    $${PWD}/OAIBastionHost.cpp \
    $${PWD}/OAIBastionHostIPConfiguration.cpp \
    $${PWD}/OAIBastionHostIPConfigurationPropertiesFormat.cpp \
    $${PWD}/OAIBastionHostIPConfigurationPropertiesFormat_publicIPAddress.cpp \
    $${PWD}/OAIBastionHostListResult.cpp \
    $${PWD}/OAIBastionHostPropertiesFormat.cpp \
# APIs
    $${PWD}/OAIBastionHostsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
