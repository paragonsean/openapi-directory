QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIKey.h \
    $${PWD}/OAIKeyListResult.h \
    $${PWD}/OAIKeyValue.h \
    $${PWD}/OAIKeyValueListResult.h \
    $${PWD}/OAILabel.h \
    $${PWD}/OAILabelListResult.h \
# APIs
    $${PWD}/OAIKeyValuesApi.h \
    $${PWD}/OAIKeysApi.h \
    $${PWD}/OAILabelsApi.h \
    $${PWD}/OAILocksApi.h \
    $${PWD}/OAIRevisionsApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIKey.cpp \
    $${PWD}/OAIKeyListResult.cpp \
    $${PWD}/OAIKeyValue.cpp \
    $${PWD}/OAIKeyValueListResult.cpp \
    $${PWD}/OAILabel.cpp \
    $${PWD}/OAILabelListResult.cpp \
# APIs
    $${PWD}/OAIKeyValuesApi.cpp \
    $${PWD}/OAIKeysApi.cpp \
    $${PWD}/OAILabelsApi.cpp \
    $${PWD}/OAILocksApi.cpp \
    $${PWD}/OAIRevisionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
