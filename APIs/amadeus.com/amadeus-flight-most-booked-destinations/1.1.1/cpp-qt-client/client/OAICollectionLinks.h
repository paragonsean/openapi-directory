/**
 * Flight Most Booked Destinations
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICollectionLinks.h
 *
 * 
 */

#ifndef OAICollectionLinks_H
#define OAICollectionLinks_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICollectionLinks : public OAIObject {
public:
    OAICollectionLinks();
    OAICollectionLinks(QString json);
    ~OAICollectionLinks() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFirst() const;
    void setFirst(const QString &first);
    bool is_first_Set() const;
    bool is_first_Valid() const;

    QString getLast() const;
    void setLast(const QString &last);
    bool is_last_Set() const;
    bool is_last_Valid() const;

    QString getNext() const;
    void setNext(const QString &next);
    bool is_next_Set() const;
    bool is_next_Valid() const;

    QString getPrevious() const;
    void setPrevious(const QString &previous);
    bool is_previous_Set() const;
    bool is_previous_Valid() const;

    QString getSelf() const;
    void setSelf(const QString &self);
    bool is_self_Set() const;
    bool is_self_Valid() const;

    QString getUp() const;
    void setUp(const QString &up);
    bool is_up_Set() const;
    bool is_up_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_first;
    bool m_first_isSet;
    bool m_first_isValid;

    QString m_last;
    bool m_last_isSet;
    bool m_last_isValid;

    QString m_next;
    bool m_next_isSet;
    bool m_next_isValid;

    QString m_previous;
    bool m_previous_isSet;
    bool m_previous_isValid;

    QString m_self;
    bool m_self_isSet;
    bool m_self_isValid;

    QString m_up;
    bool m_up_isSet;
    bool m_up_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICollectionLinks)

#endif // OAICollectionLinks_H
