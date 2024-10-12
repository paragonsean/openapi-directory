QT += network

HEADERS += \
# Models
    $${PWD}/OAIChangePassword.h \
    $${PWD}/OAIDates.h \
    $${PWD}/OAIFeedback.h \
    $${PWD}/OAILogin.h \
    $${PWD}/OAINewUser.h \
    $${PWD}/OAITransfer.h \
# APIs
    $${PWD}/OAIClass1LoginApi.h \
    $${PWD}/OAIClass2AccountApi.h \
    $${PWD}/OAIClass3TransferApi.h \
    $${PWD}/OAIClass4FeedbackApi.h \
    $${PWD}/OAIClass5AdminApi.h \
    $${PWD}/OAIClass6LogoutApi.h \
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
    $${PWD}/OAIChangePassword.cpp \
    $${PWD}/OAIDates.cpp \
    $${PWD}/OAIFeedback.cpp \
    $${PWD}/OAILogin.cpp \
    $${PWD}/OAINewUser.cpp \
    $${PWD}/OAITransfer.cpp \
# APIs
    $${PWD}/OAIClass1LoginApi.cpp \
    $${PWD}/OAIClass2AccountApi.cpp \
    $${PWD}/OAIClass3TransferApi.cpp \
    $${PWD}/OAIClass4FeedbackApi.cpp \
    $${PWD}/OAIClass5AdminApi.cpp \
    $${PWD}/OAIClass6LogoutApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
