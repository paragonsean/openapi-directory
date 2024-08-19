/**
 * AWS Health Imaging
 * <p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2023-07-19
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICopyImageSetResponse.h"
#include "OAICopyImageSet_request.h"
#include "OAICreateDatastoreResponse.h"
#include "OAICreateDatastore_request.h"
#include "OAIDeleteDatastoreResponse.h"
#include "OAIDeleteImageSetResponse.h"
#include "OAIGetDICOMImportJobResponse.h"
#include "OAIGetDatastoreResponse.h"
#include "OAIGetImageFrameResponse.h"
#include "OAIGetImageFrame_request.h"
#include "OAIGetImageSetMetadataResponse.h"
#include "OAIGetImageSetResponse.h"
#include "OAIListDICOMImportJobsResponse.h"
#include "OAIListDatastoresResponse.h"
#include "OAIListImageSetVersionsResponse.h"
#include "OAIListTagsForResourceResponse.h"
#include "OAIObject.h"
#include "OAISearchImageSetsResponse.h"
#include "OAISearchImageSets_request.h"
#include "OAIStartDICOMImportJobResponse.h"
#include "OAIStartDICOMImportJob_request.h"
#include "OAITagResource_request.h"
#include "OAIUpdateImageSetMetadataResponse.h"
#include "OAIUpdateImageSetMetadata_request.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  source_image_set_id QString [required]
    * @param[in]  oai_copy_image_set_request OAICopyImageSet_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void copyImageSet(const QString &datastore_id, const QString &source_image_set_id, const OAICopyImageSet_request &oai_copy_image_set_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_datastore_request OAICreateDatastore_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createDatastore(const OAICreateDatastore_request &oai_create_datastore_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteDatastore(const QString &datastore_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  image_set_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteImageSet(const QString &datastore_id, const QString &image_set_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  job_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getDICOMImportJob(const QString &datastore_id, const QString &job_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getDatastore(const QString &datastore_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  image_set_id QString [required]
    * @param[in]  oai_get_image_frame_request OAIGetImageFrame_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getImageFrame(const QString &datastore_id, const QString &image_set_id, const OAIGetImageFrame_request &oai_get_image_frame_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  image_set_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  version QString [optional]
    */
    virtual void getImageSet(const QString &datastore_id, const QString &image_set_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &version = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  image_set_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  version QString [optional]
    */
    virtual void getImageSetMetadata(const QString &datastore_id, const QString &image_set_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &version = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  job_status QString [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  max_results qint32 [optional]
    */
    virtual void listDICOMImportJobs(const QString &datastore_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &job_status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  datastore_status QString [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  max_results qint32 [optional]
    */
    virtual void listDatastores(const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &datastore_status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  image_set_id QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  max_results qint32 [optional]
    */
    virtual void listImageSetVersions(const QString &datastore_id, const QString &image_set_id, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void listTagsForResource(const QString &resource_arn, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  oai_search_image_sets_request OAISearchImageSets_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void searchImageSets(const QString &datastore_id, const OAISearchImageSets_request &oai_search_image_sets_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  oai_start_dicom_import_job_request OAIStartDICOMImportJob_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void startDICOMImportJob(const QString &datastore_id, const OAIStartDICOMImportJob_request &oai_start_dicom_import_job_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  oai_tag_resource_request OAITagResource_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void tagResource(const QString &resource_arn, const OAITagResource_request &oai_tag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  tag_keys QList<QString> [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void untagResource(const QString &resource_arn, const QList<QString> &tag_keys, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  datastore_id QString [required]
    * @param[in]  image_set_id QString [required]
    * @param[in]  latest_version QString [required]
    * @param[in]  oai_update_image_set_metadata_request OAIUpdateImageSetMetadata_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateImageSetMetadata(const QString &datastore_id, const QString &image_set_id, const QString &latest_version, const OAIUpdateImageSetMetadata_request &oai_update_image_set_metadata_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void copyImageSetCallback(OAIHttpRequestWorker *worker);
    void createDatastoreCallback(OAIHttpRequestWorker *worker);
    void deleteDatastoreCallback(OAIHttpRequestWorker *worker);
    void deleteImageSetCallback(OAIHttpRequestWorker *worker);
    void getDICOMImportJobCallback(OAIHttpRequestWorker *worker);
    void getDatastoreCallback(OAIHttpRequestWorker *worker);
    void getImageFrameCallback(OAIHttpRequestWorker *worker);
    void getImageSetCallback(OAIHttpRequestWorker *worker);
    void getImageSetMetadataCallback(OAIHttpRequestWorker *worker);
    void listDICOMImportJobsCallback(OAIHttpRequestWorker *worker);
    void listDatastoresCallback(OAIHttpRequestWorker *worker);
    void listImageSetVersionsCallback(OAIHttpRequestWorker *worker);
    void listTagsForResourceCallback(OAIHttpRequestWorker *worker);
    void searchImageSetsCallback(OAIHttpRequestWorker *worker);
    void startDICOMImportJobCallback(OAIHttpRequestWorker *worker);
    void tagResourceCallback(OAIHttpRequestWorker *worker);
    void untagResourceCallback(OAIHttpRequestWorker *worker);
    void updateImageSetMetadataCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void copyImageSetSignal(OAICopyImageSetResponse summary);
    void createDatastoreSignal(OAICreateDatastoreResponse summary);
    void deleteDatastoreSignal(OAIDeleteDatastoreResponse summary);
    void deleteImageSetSignal(OAIDeleteImageSetResponse summary);
    void getDICOMImportJobSignal(OAIGetDICOMImportJobResponse summary);
    void getDatastoreSignal(OAIGetDatastoreResponse summary);
    void getImageFrameSignal(OAIGetImageFrameResponse summary);
    void getImageSetSignal(OAIGetImageSetResponse summary);
    void getImageSetMetadataSignal(OAIGetImageSetMetadataResponse summary);
    void listDICOMImportJobsSignal(OAIListDICOMImportJobsResponse summary);
    void listDatastoresSignal(OAIListDatastoresResponse summary);
    void listImageSetVersionsSignal(OAIListImageSetVersionsResponse summary);
    void listTagsForResourceSignal(OAIListTagsForResourceResponse summary);
    void searchImageSetsSignal(OAISearchImageSetsResponse summary);
    void startDICOMImportJobSignal(OAIStartDICOMImportJobResponse summary);
    void tagResourceSignal(OAIObject summary);
    void untagResourceSignal(OAIObject summary);
    void updateImageSetMetadataSignal(OAIUpdateImageSetMetadataResponse summary);


    void copyImageSetSignalFull(OAIHttpRequestWorker *worker, OAICopyImageSetResponse summary);
    void createDatastoreSignalFull(OAIHttpRequestWorker *worker, OAICreateDatastoreResponse summary);
    void deleteDatastoreSignalFull(OAIHttpRequestWorker *worker, OAIDeleteDatastoreResponse summary);
    void deleteImageSetSignalFull(OAIHttpRequestWorker *worker, OAIDeleteImageSetResponse summary);
    void getDICOMImportJobSignalFull(OAIHttpRequestWorker *worker, OAIGetDICOMImportJobResponse summary);
    void getDatastoreSignalFull(OAIHttpRequestWorker *worker, OAIGetDatastoreResponse summary);
    void getImageFrameSignalFull(OAIHttpRequestWorker *worker, OAIGetImageFrameResponse summary);
    void getImageSetSignalFull(OAIHttpRequestWorker *worker, OAIGetImageSetResponse summary);
    void getImageSetMetadataSignalFull(OAIHttpRequestWorker *worker, OAIGetImageSetMetadataResponse summary);
    void listDICOMImportJobsSignalFull(OAIHttpRequestWorker *worker, OAIListDICOMImportJobsResponse summary);
    void listDatastoresSignalFull(OAIHttpRequestWorker *worker, OAIListDatastoresResponse summary);
    void listImageSetVersionsSignalFull(OAIHttpRequestWorker *worker, OAIListImageSetVersionsResponse summary);
    void listTagsForResourceSignalFull(OAIHttpRequestWorker *worker, OAIListTagsForResourceResponse summary);
    void searchImageSetsSignalFull(OAIHttpRequestWorker *worker, OAISearchImageSetsResponse summary);
    void startDICOMImportJobSignalFull(OAIHttpRequestWorker *worker, OAIStartDICOMImportJobResponse summary);
    void tagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void untagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateImageSetMetadataSignalFull(OAIHttpRequestWorker *worker, OAIUpdateImageSetMetadataResponse summary);

    Q_DECL_DEPRECATED_X("Use copyImageSetSignalError() instead")
    void copyImageSetSignalE(OAICopyImageSetResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void copyImageSetSignalError(OAICopyImageSetResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createDatastoreSignalError() instead")
    void createDatastoreSignalE(OAICreateDatastoreResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createDatastoreSignalError(OAICreateDatastoreResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatastoreSignalError() instead")
    void deleteDatastoreSignalE(OAIDeleteDatastoreResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatastoreSignalError(OAIDeleteDatastoreResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteImageSetSignalError() instead")
    void deleteImageSetSignalE(OAIDeleteImageSetResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteImageSetSignalError(OAIDeleteImageSetResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDICOMImportJobSignalError() instead")
    void getDICOMImportJobSignalE(OAIGetDICOMImportJobResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDICOMImportJobSignalError(OAIGetDICOMImportJobResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatastoreSignalError() instead")
    void getDatastoreSignalE(OAIGetDatastoreResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatastoreSignalError(OAIGetDatastoreResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getImageFrameSignalError() instead")
    void getImageFrameSignalE(OAIGetImageFrameResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getImageFrameSignalError(OAIGetImageFrameResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getImageSetSignalError() instead")
    void getImageSetSignalE(OAIGetImageSetResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getImageSetSignalError(OAIGetImageSetResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getImageSetMetadataSignalError() instead")
    void getImageSetMetadataSignalE(OAIGetImageSetMetadataResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getImageSetMetadataSignalError(OAIGetImageSetMetadataResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDICOMImportJobsSignalError() instead")
    void listDICOMImportJobsSignalE(OAIListDICOMImportJobsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listDICOMImportJobsSignalError(OAIListDICOMImportJobsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDatastoresSignalError() instead")
    void listDatastoresSignalE(OAIListDatastoresResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listDatastoresSignalError(OAIListDatastoresResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listImageSetVersionsSignalError() instead")
    void listImageSetVersionsSignalE(OAIListImageSetVersionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listImageSetVersionsSignalError(OAIListImageSetVersionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalError() instead")
    void listTagsForResourceSignalE(OAIListTagsForResourceResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalError(OAIListTagsForResourceResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchImageSetsSignalError() instead")
    void searchImageSetsSignalE(OAISearchImageSetsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void searchImageSetsSignalError(OAISearchImageSetsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use startDICOMImportJobSignalError() instead")
    void startDICOMImportJobSignalE(OAIStartDICOMImportJobResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void startDICOMImportJobSignalError(OAIStartDICOMImportJobResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalError() instead")
    void tagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalError() instead")
    void untagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateImageSetMetadataSignalError() instead")
    void updateImageSetMetadataSignalE(OAIUpdateImageSetMetadataResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateImageSetMetadataSignalError(OAIUpdateImageSetMetadataResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use copyImageSetSignalErrorFull() instead")
    void copyImageSetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void copyImageSetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createDatastoreSignalErrorFull() instead")
    void createDatastoreSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createDatastoreSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatastoreSignalErrorFull() instead")
    void deleteDatastoreSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatastoreSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteImageSetSignalErrorFull() instead")
    void deleteImageSetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteImageSetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDICOMImportJobSignalErrorFull() instead")
    void getDICOMImportJobSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDICOMImportJobSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatastoreSignalErrorFull() instead")
    void getDatastoreSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatastoreSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getImageFrameSignalErrorFull() instead")
    void getImageFrameSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getImageFrameSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getImageSetSignalErrorFull() instead")
    void getImageSetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getImageSetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getImageSetMetadataSignalErrorFull() instead")
    void getImageSetMetadataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getImageSetMetadataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDICOMImportJobsSignalErrorFull() instead")
    void listDICOMImportJobsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listDICOMImportJobsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDatastoresSignalErrorFull() instead")
    void listDatastoresSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listDatastoresSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listImageSetVersionsSignalErrorFull() instead")
    void listImageSetVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listImageSetVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalErrorFull() instead")
    void listTagsForResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchImageSetsSignalErrorFull() instead")
    void searchImageSetsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void searchImageSetsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use startDICOMImportJobSignalErrorFull() instead")
    void startDICOMImportJobSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void startDICOMImportJobSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalErrorFull() instead")
    void tagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalErrorFull() instead")
    void untagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateImageSetMetadataSignalErrorFull() instead")
    void updateImageSetMetadataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateImageSetMetadataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
