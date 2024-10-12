QT += network

HEADERS += \
# Models
    $${PWD}/OAIDirectoryTenant.h \
    $${PWD}/OAIDirectoryTenantList.h \
    $${PWD}/OAIDirectoryTenantProperties.h \
# APIs
    $${PWD}/OAIDirectoryTenantsApi.h \
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
    $${PWD}/OAIDirectoryTenant.cpp \
    $${PWD}/OAIDirectoryTenantList.cpp \
    $${PWD}/OAIDirectoryTenantProperties.cpp \
# APIs
    $${PWD}/OAIDirectoryTenantsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
