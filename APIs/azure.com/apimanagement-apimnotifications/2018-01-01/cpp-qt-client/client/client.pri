QT += network

HEADERS += \
# Models
    $${PWD}/OAINotificationCollection.h \
    $${PWD}/OAINotificationContract.h \
    $${PWD}/OAINotificationContractProperties.h \
    $${PWD}/OAINotification_Get_default_response.h \
    $${PWD}/OAINotification_Get_default_response_error.h \
    $${PWD}/OAINotification_Get_default_response_error_details_inner.h \
    $${PWD}/OAIRecipientEmailCollection.h \
    $${PWD}/OAIRecipientEmailContract.h \
    $${PWD}/OAIRecipientEmailContractProperties.h \
    $${PWD}/OAIRecipientUserCollection.h \
    $${PWD}/OAIRecipientUserContract.h \
    $${PWD}/OAIRecipientUsersContractProperties.h \
    $${PWD}/OAIRecipientsContractProperties.h \
# APIs
    $${PWD}/OAINotificationApi.h \
    $${PWD}/OAINotificationRecipientEmailApi.h \
    $${PWD}/OAINotificationRecipientUserApi.h \
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
    $${PWD}/OAINotificationCollection.cpp \
    $${PWD}/OAINotificationContract.cpp \
    $${PWD}/OAINotificationContractProperties.cpp \
    $${PWD}/OAINotification_Get_default_response.cpp \
    $${PWD}/OAINotification_Get_default_response_error.cpp \
    $${PWD}/OAINotification_Get_default_response_error_details_inner.cpp \
    $${PWD}/OAIRecipientEmailCollection.cpp \
    $${PWD}/OAIRecipientEmailContract.cpp \
    $${PWD}/OAIRecipientEmailContractProperties.cpp \
    $${PWD}/OAIRecipientUserCollection.cpp \
    $${PWD}/OAIRecipientUserContract.cpp \
    $${PWD}/OAIRecipientUsersContractProperties.cpp \
    $${PWD}/OAIRecipientsContractProperties.cpp \
# APIs
    $${PWD}/OAINotificationApi.cpp \
    $${PWD}/OAINotificationRecipientEmailApi.cpp \
    $${PWD}/OAINotificationRecipientUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
