QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiResponse.h \
    $${PWD}/OAIFindings_inner.h \
    $${PWD}/OAIFindings_inner_meta_risk.h \
    $${PWD}/OAIFindings_inner_meta_vuln_refs.h \
    $${PWD}/OAIScanDefinition.h \
    $${PWD}/OAIScanDefinition_assets_inner.h \
# APIs
    $${PWD}/OAIPatrowlEngineApi.h \
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
    $${PWD}/OAIApiResponse.cpp \
    $${PWD}/OAIFindings_inner.cpp \
    $${PWD}/OAIFindings_inner_meta_risk.cpp \
    $${PWD}/OAIFindings_inner_meta_vuln_refs.cpp \
    $${PWD}/OAIScanDefinition.cpp \
    $${PWD}/OAIScanDefinition_assets_inner.cpp \
# APIs
    $${PWD}/OAIPatrowlEngineApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
