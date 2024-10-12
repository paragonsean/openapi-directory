QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiv1_0_SafeUnsafeImageWithTags_body.h \
    $${PWD}/OAIInline_response_200.h \
    $${PWD}/OAIInline_response_200_predictions.h \
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
    $${PWD}/OAIApiv1_0_SafeUnsafeImageWithTags_body.cpp \
    $${PWD}/OAIInline_response_200.cpp \
    $${PWD}/OAIInline_response_200_predictions.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
