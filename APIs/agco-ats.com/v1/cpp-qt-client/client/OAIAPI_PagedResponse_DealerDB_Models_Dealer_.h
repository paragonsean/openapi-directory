/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAPI_PagedResponse_DealerDB_Models_Dealer_.h
 *
 * A response containing a page of results and metadata concerning the results
 */

#ifndef OAIAPI_PagedResponse_DealerDB_Models_Dealer__H
#define OAIAPI_PagedResponse_DealerDB_Models_Dealer__H

#include <QJsonObject>

#include "OAIAPI_PagedResponseMetadata.h"
#include "OAIDealerDB_Models_Dealer.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDealerDB_Models_Dealer;
class OAIAPI_PagedResponseMetadata;

class OAIAPI_PagedResponse_DealerDB_Models_Dealer_ : public OAIObject {
public:
    OAIAPI_PagedResponse_DealerDB_Models_Dealer_();
    OAIAPI_PagedResponse_DealerDB_Models_Dealer_(QString json);
    ~OAIAPI_PagedResponse_DealerDB_Models_Dealer_() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDealerDB_Models_Dealer> getEntities() const;
    void setEntities(const QList<OAIDealerDB_Models_Dealer> &entities);
    bool is_entities_Set() const;
    bool is_entities_Valid() const;

    OAIAPI_PagedResponseMetadata getMetadata() const;
    void setMetadata(const OAIAPI_PagedResponseMetadata &metadata);
    bool is_metadata_Set() const;
    bool is_metadata_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDealerDB_Models_Dealer> m_entities;
    bool m_entities_isSet;
    bool m_entities_isValid;

    OAIAPI_PagedResponseMetadata m_metadata;
    bool m_metadata_isSet;
    bool m_metadata_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAPI_PagedResponse_DealerDB_Models_Dealer_)

#endif // OAIAPI_PagedResponse_DealerDB_Models_Dealer__H
