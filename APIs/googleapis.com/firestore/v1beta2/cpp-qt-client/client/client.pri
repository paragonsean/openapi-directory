QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleFirestoreAdminV1Progress.h \
    $${PWD}/OAIGoogleFirestoreAdminV1RestoreDatabaseMetadata.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ExportDocumentsMetadata.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ExportDocumentsRequest.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ExportDocumentsResponse.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2Field.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2FieldOperationMetadata.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ImportDocumentsMetadata.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ImportDocumentsRequest.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2Index.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexConfig.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexConfigDelta.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexField.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexOperationMetadata.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ListFieldsResponse.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ListIndexesResponse.h \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2Progress.h \
    $${PWD}/OAIGoogleLongrunningOperation.h \
    $${PWD}/OAIStatus.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGoogleFirestoreAdminV1Progress.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1RestoreDatabaseMetadata.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ExportDocumentsMetadata.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ExportDocumentsRequest.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ExportDocumentsResponse.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2Field.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2FieldOperationMetadata.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ImportDocumentsMetadata.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ImportDocumentsRequest.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2Index.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexConfig.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexConfigDelta.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexField.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2IndexOperationMetadata.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ListFieldsResponse.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2ListIndexesResponse.cpp \
    $${PWD}/OAIGoogleFirestoreAdminV1beta2Progress.cpp \
    $${PWD}/OAIGoogleLongrunningOperation.cpp \
    $${PWD}/OAIStatus.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
