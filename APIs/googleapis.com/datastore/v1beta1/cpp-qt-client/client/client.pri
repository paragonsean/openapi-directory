QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleDatastoreAdminV1CommonMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1EntityFilter.h \
    $${PWD}/OAIGoogleDatastoreAdminV1ExportEntitiesMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1ExportEntitiesResponse.h \
    $${PWD}/OAIGoogleDatastoreAdminV1ImportEntitiesMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1IndexOperationMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1MigrationProgressEvent.h \
    $${PWD}/OAIGoogleDatastoreAdminV1MigrationStateEvent.h \
    $${PWD}/OAIGoogleDatastoreAdminV1PrepareStepDetails.h \
    $${PWD}/OAIGoogleDatastoreAdminV1Progress.h \
    $${PWD}/OAIGoogleDatastoreAdminV1RedirectWritesStepDetails.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1CommonMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1EntityFilter.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ExportEntitiesMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ExportEntitiesRequest.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ExportEntitiesResponse.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ImportEntitiesMetadata.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ImportEntitiesRequest.h \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1Progress.h \
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
    $${PWD}/OAIGoogleDatastoreAdminV1CommonMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1EntityFilter.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1ExportEntitiesMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1ExportEntitiesResponse.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1ImportEntitiesMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1IndexOperationMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1MigrationProgressEvent.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1MigrationStateEvent.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1PrepareStepDetails.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1Progress.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1RedirectWritesStepDetails.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1CommonMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1EntityFilter.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ExportEntitiesMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ExportEntitiesRequest.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ExportEntitiesResponse.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ImportEntitiesMetadata.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1ImportEntitiesRequest.cpp \
    $${PWD}/OAIGoogleDatastoreAdminV1beta1Progress.cpp \
    $${PWD}/OAIGoogleLongrunningOperation.cpp \
    $${PWD}/OAIStatus.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
