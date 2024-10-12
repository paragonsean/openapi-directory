QT += network

HEADERS += \
# Models
    $${PWD}/OAIATMDefinition.h \
    $${PWD}/OAIATMDefinitionMeta.h \
    $${PWD}/OAIATM_inner.h \
    $${PWD}/OAIBrand_inner.h \
    $${PWD}/OAIErrorDefinition400.h \
    $${PWD}/OAIErrorDefinition408.h \
    $${PWD}/OAIErrorDefinition429.h \
    $${PWD}/OAIErrorDefinition500.h \
    $${PWD}/OAIErrorDefinition503.h \
    $${PWD}/OAIMetaDefinition.h \
    $${PWD}/OAIOtherATMServices_inner.h \
    $${PWD}/OAIOtherAccessibility_inner.h \
# APIs
    $${PWD}/OAIATMsApi.h \
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
    $${PWD}/OAIATMDefinition.cpp \
    $${PWD}/OAIATMDefinitionMeta.cpp \
    $${PWD}/OAIATM_inner.cpp \
    $${PWD}/OAIBrand_inner.cpp \
    $${PWD}/OAIErrorDefinition400.cpp \
    $${PWD}/OAIErrorDefinition408.cpp \
    $${PWD}/OAIErrorDefinition429.cpp \
    $${PWD}/OAIErrorDefinition500.cpp \
    $${PWD}/OAIErrorDefinition503.cpp \
    $${PWD}/OAIMetaDefinition.cpp \
    $${PWD}/OAIOtherATMServices_inner.cpp \
    $${PWD}/OAIOtherAccessibility_inner.cpp \
# APIs
    $${PWD}/OAIATMsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
