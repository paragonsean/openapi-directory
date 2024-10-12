QT += network

HEADERS += \
# Models
    $${PWD}/OAIPublicIPPrefix.h \
    $${PWD}/OAIPublicIPPrefixListResult.h \
    $${PWD}/OAIPublicIPPrefixPropertiesFormat.h \
    $${PWD}/OAIPublicIPPrefixPropertiesFormat_ipTags_inner.h \
    $${PWD}/OAIPublicIPPrefixPropertiesFormat_loadBalancerFrontendIpConfiguration.h \
    $${PWD}/OAIPublicIPPrefixSku.h \
    $${PWD}/OAIPublicIPPrefixes_UpdateTags_request.h \
    $${PWD}/OAIReferencedPublicIpAddress.h \
# APIs
    $${PWD}/OAIPublicIPPrefixesApi.h \
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
    $${PWD}/OAIPublicIPPrefix.cpp \
    $${PWD}/OAIPublicIPPrefixListResult.cpp \
    $${PWD}/OAIPublicIPPrefixPropertiesFormat.cpp \
    $${PWD}/OAIPublicIPPrefixPropertiesFormat_ipTags_inner.cpp \
    $${PWD}/OAIPublicIPPrefixPropertiesFormat_loadBalancerFrontendIpConfiguration.cpp \
    $${PWD}/OAIPublicIPPrefixSku.cpp \
    $${PWD}/OAIPublicIPPrefixes_UpdateTags_request.cpp \
    $${PWD}/OAIReferencedPublicIpAddress.cpp \
# APIs
    $${PWD}/OAIPublicIPPrefixesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
