QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateUserResponse.h \
    $${PWD}/OAIInvalidToken.h \
    $${PWD}/OAIKeyFailure.h \
    $${PWD}/OAILoginResponse.h \
    $${PWD}/OAIRequestPasswordResetResponse.h \
    $${PWD}/OAISample.h \
    $${PWD}/OAISample_1.h \
    $${PWD}/OAISample_2.h \
    $${PWD}/OAISample_3.h \
    $${PWD}/OAISample_4.h \
    $${PWD}/OAISignin.h \
    $${PWD}/OAISigninResponse.h \
    $${PWD}/OAIUserRecord.h \
# APIs
    $${PWD}/OAIAttendeesSigninsApi.h \
    $${PWD}/OAIAuthenticationApi.h \
    $${PWD}/OAIPasswordsApi.h \
    $${PWD}/OAITeamMembersApi.h \
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
    $${PWD}/OAICreateUserResponse.cpp \
    $${PWD}/OAIInvalidToken.cpp \
    $${PWD}/OAIKeyFailure.cpp \
    $${PWD}/OAILoginResponse.cpp \
    $${PWD}/OAIRequestPasswordResetResponse.cpp \
    $${PWD}/OAISample.cpp \
    $${PWD}/OAISample_1.cpp \
    $${PWD}/OAISample_2.cpp \
    $${PWD}/OAISample_3.cpp \
    $${PWD}/OAISample_4.cpp \
    $${PWD}/OAISignin.cpp \
    $${PWD}/OAISigninResponse.cpp \
    $${PWD}/OAIUserRecord.cpp \
# APIs
    $${PWD}/OAIAttendeesSigninsApi.cpp \
    $${PWD}/OAIAuthenticationApi.cpp \
    $${PWD}/OAIPasswordsApi.cpp \
    $${PWD}/OAITeamMembersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
