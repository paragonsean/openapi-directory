/**
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIObjectStoreSearchResult.h
 *
 * 
 */

#ifndef OAIObjectStoreSearchResult_H
#define OAIObjectStoreSearchResult_H

#include <QJsonObject>

#include "OAIObjectStoreSearchResult_hits.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIObjectStoreSearchResult_hits;

class OAIObjectStoreSearchResult : public OAIObject {
public:
    OAIObjectStoreSearchResult();
    OAIObjectStoreSearchResult(QString json);
    ~OAIObjectStoreSearchResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObjectStoreSearchResult_hits getHits() const;
    void setHits(const OAIObjectStoreSearchResult_hits &hits);
    bool is_hits_Set() const;
    bool is_hits_Valid() const;

    bool isTimedOut() const;
    void setTimedOut(const bool &timed_out);
    bool is_timed_out_Set() const;
    bool is_timed_out_Valid() const;

    qint32 getTook() const;
    void setTook(const qint32 &took);
    bool is_took_Set() const;
    bool is_took_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObjectStoreSearchResult_hits m_hits;
    bool m_hits_isSet;
    bool m_hits_isValid;

    bool m_timed_out;
    bool m_timed_out_isSet;
    bool m_timed_out_isValid;

    qint32 m_took;
    bool m_took_isSet;
    bool m_took_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIObjectStoreSearchResult)

#endif // OAIObjectStoreSearchResult_H
