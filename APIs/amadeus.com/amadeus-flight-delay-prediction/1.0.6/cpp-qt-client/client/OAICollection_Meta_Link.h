/**
 * Flight Delay Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.6
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICollection_Meta_Link.h
 *
 * 
 */

#ifndef OAICollection_Meta_Link_H
#define OAICollection_Meta_Link_H

#include <QJsonObject>

#include "OAICollectionLinks.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICollectionLinks;

class OAICollection_Meta_Link : public OAIObject {
public:
    OAICollection_Meta_Link();
    OAICollection_Meta_Link(QString json);
    ~OAICollection_Meta_Link() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    OAICollectionLinks getLinks() const;
    void setLinks(const OAICollectionLinks &links);
    bool is_links_Set() const;
    bool is_links_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    OAICollectionLinks m_links;
    bool m_links_isSet;
    bool m_links_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICollection_Meta_Link)

#endif // OAICollection_Meta_Link_H
