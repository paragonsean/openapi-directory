QT += network

HEADERS += \
# Models
    $${PWD}/OAIBox.h \
    $${PWD}/OAIBoxProperties.h \
    $${PWD}/OAIBoxType.h \
    $${PWD}/OAIBoxTypeSet.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItemProperties.h \
    $${PWD}/OAIItemSet.h \
    $${PWD}/OAIPack.h \
    $${PWD}/OAIPackResponse.h \
    $${PWD}/OAIPoint.h \
    $${PWD}/OAIRateTable.h \
    $${PWD}/OAIRule.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIBox.cpp \
    $${PWD}/OAIBoxProperties.cpp \
    $${PWD}/OAIBoxType.cpp \
    $${PWD}/OAIBoxTypeSet.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItemProperties.cpp \
    $${PWD}/OAIItemSet.cpp \
    $${PWD}/OAIPack.cpp \
    $${PWD}/OAIPackResponse.cpp \
    $${PWD}/OAIPoint.cpp \
    $${PWD}/OAIRateTable.cpp \
    $${PWD}/OAIRule.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
