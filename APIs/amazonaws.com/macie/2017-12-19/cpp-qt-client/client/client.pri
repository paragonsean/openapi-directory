QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssociateMemberAccountRequest.h \
    $${PWD}/OAIAssociateS3ResourcesRequest.h \
    $${PWD}/OAIAssociateS3ResourcesResult.h \
    $${PWD}/OAIClassificationType.h \
    $${PWD}/OAIClassificationTypeUpdate.h \
    $${PWD}/OAIDisassociateMemberAccountRequest.h \
    $${PWD}/OAIDisassociateS3ResourcesRequest.h \
    $${PWD}/OAIDisassociateS3ResourcesResult.h \
    $${PWD}/OAIFailedS3Resource.h \
    $${PWD}/OAIFailedS3Resource_failedItem.h \
    $${PWD}/OAIListMemberAccountsRequest.h \
    $${PWD}/OAIListMemberAccountsResult.h \
    $${PWD}/OAIListS3ResourcesRequest.h \
    $${PWD}/OAIListS3ResourcesResult.h \
    $${PWD}/OAIMemberAccount.h \
    $${PWD}/OAIS3ContinuousClassificationType.h \
    $${PWD}/OAIS3OneTimeClassificationType.h \
    $${PWD}/OAIS3Resource.h \
    $${PWD}/OAIS3ResourceClassification.h \
    $${PWD}/OAIS3ResourceClassificationUpdate.h \
    $${PWD}/OAIS3ResourceClassificationUpdate_classificationTypeUpdate.h \
    $${PWD}/OAIS3ResourceClassification_classificationType.h \
    $${PWD}/OAIUpdateS3ResourcesRequest.h \
    $${PWD}/OAIUpdateS3ResourcesResult.h \
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
    $${PWD}/OAIAssociateMemberAccountRequest.cpp \
    $${PWD}/OAIAssociateS3ResourcesRequest.cpp \
    $${PWD}/OAIAssociateS3ResourcesResult.cpp \
    $${PWD}/OAIClassificationType.cpp \
    $${PWD}/OAIClassificationTypeUpdate.cpp \
    $${PWD}/OAIDisassociateMemberAccountRequest.cpp \
    $${PWD}/OAIDisassociateS3ResourcesRequest.cpp \
    $${PWD}/OAIDisassociateS3ResourcesResult.cpp \
    $${PWD}/OAIFailedS3Resource.cpp \
    $${PWD}/OAIFailedS3Resource_failedItem.cpp \
    $${PWD}/OAIListMemberAccountsRequest.cpp \
    $${PWD}/OAIListMemberAccountsResult.cpp \
    $${PWD}/OAIListS3ResourcesRequest.cpp \
    $${PWD}/OAIListS3ResourcesResult.cpp \
    $${PWD}/OAIMemberAccount.cpp \
    $${PWD}/OAIS3ContinuousClassificationType.cpp \
    $${PWD}/OAIS3OneTimeClassificationType.cpp \
    $${PWD}/OAIS3Resource.cpp \
    $${PWD}/OAIS3ResourceClassification.cpp \
    $${PWD}/OAIS3ResourceClassificationUpdate.cpp \
    $${PWD}/OAIS3ResourceClassificationUpdate_classificationTypeUpdate.cpp \
    $${PWD}/OAIS3ResourceClassification_classificationType.cpp \
    $${PWD}/OAIUpdateS3ResourcesRequest.cpp \
    $${PWD}/OAIUpdateS3ResourcesResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
