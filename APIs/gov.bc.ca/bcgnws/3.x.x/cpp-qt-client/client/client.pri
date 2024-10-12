QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIFeatureApi.h \
    $${PWD}/OAIFeatureTaxonomyApi.h \
    $${PWD}/OAINameApi.h \
    $${PWD}/OAINameAuthorityApi.h \
    $${PWD}/OAISearchApi.h \
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
# APIs
    $${PWD}/OAIFeatureApi.cpp \
    $${PWD}/OAIFeatureTaxonomyApi.cpp \
    $${PWD}/OAINameApi.cpp \
    $${PWD}/OAINameAuthorityApi.cpp \
    $${PWD}/OAISearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
