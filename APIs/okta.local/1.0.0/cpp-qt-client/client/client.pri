QT += network

HEADERS += \
# Models
    $${PWD}/OAIChangePassword_request.h \
    $${PWD}/OAIChangePassword_request_newPassword.h \
    $${PWD}/OAIChangePassword_request_oldPassword.h \
    $${PWD}/OAIChangeRecoveryQuestion_request.h \
    $${PWD}/OAIChangeRecoveryQuestion_request_recovery_question.h \
    $${PWD}/OAICreateUserInGroup_request.h \
    $${PWD}/OAICreateUserInGroup_request_profile.h \
    $${PWD}/OAISetRecoveryCredential_request.h \
    $${PWD}/OAISetRecoveryCredential_request_credentials.h \
    $${PWD}/OAISetRecoveryCredential_request_credentials_recovery_question.h \
# APIs
    $${PWD}/OAICreateUserApi.h \
    $${PWD}/OAICredentialOperationsApi.h \
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAILifecycleOperationsApi.h \
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
    $${PWD}/OAIChangePassword_request.cpp \
    $${PWD}/OAIChangePassword_request_newPassword.cpp \
    $${PWD}/OAIChangePassword_request_oldPassword.cpp \
    $${PWD}/OAIChangeRecoveryQuestion_request.cpp \
    $${PWD}/OAIChangeRecoveryQuestion_request_recovery_question.cpp \
    $${PWD}/OAICreateUserInGroup_request.cpp \
    $${PWD}/OAICreateUserInGroup_request_profile.cpp \
    $${PWD}/OAISetRecoveryCredential_request.cpp \
    $${PWD}/OAISetRecoveryCredential_request_credentials.cpp \
    $${PWD}/OAISetRecoveryCredential_request_credentials_recovery_question.cpp \
# APIs
    $${PWD}/OAICreateUserApi.cpp \
    $${PWD}/OAICredentialOperationsApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAILifecycleOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
