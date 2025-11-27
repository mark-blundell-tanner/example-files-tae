<!-- Prüfen Sie diese Datei anhand der Datei leitfaden.md -->

# API Referenz

# Einführung

Diese Dokumentation beschreibt die REST API für unser System. Die API ermöglicht es Entwicklern auf die Funktionen des Systems zuzugreifen und eigene Anwendungen zu erstellen.

## Authentifizierung

Für die Authentifizierung verwenden Sie einen API-Schlüssel den Sie in Ihrem Benutzerkonto generieren können. Der Schlüssel muss bei jeder Anfrage im Header mitgesendet werden.

**Beispiel**:

```python
import requests

response = requests.get('https://api.example.com/data',
    headers={'Authorization': 'Bearer YOUR_API_KEY'}
```

### Endpunkte

#### GET /users

Gibt eine Liste aller Benutzer zurück die im System registriert sind.

Parameter:
| Name | Typ | Beschreibung |
|---|---|---|
|limit|integer|maximale Anzahl|
|offset|integer|Startposition|
|filter|string|Filterkriterien|

##### Response

```json
{
    "users": [
        {"id": 1, "name": "Max"},
        {"id": 2, "name": "Anna"}
    ]
}
```


#### POST /users

Erstellt einen neuen Benutzer.

**Request Body**:

```
{
    "name": "string",
    "email": "string",
    "role": "string"
}
```

**Wichtig**: Alle Felder sind Pflichtfelder!!!

## Fehlerbehandlung

Die API gibt Standard-HTTP-Statuscodes zurück:

- ```200``` - Erfolg
- ```400``` - Ungültige Anfrage
- ```401``` - Nicht authentifiziert
- ```404``` - Nicht gefunden
- ```500``` - Serverfehler

Fehlerantworten enthalten zusätzliche Informationen im JSON-Format.

### Rate Limiting

Die API ist auf 1000 Anfragen pro Stunde begrenzt. Wenn Sie dieses Limit überschreiten erhalten Sie einen `429` Fehlercode.

![](diagram.png)

## Webhooks

Sie können Webhooks konfigurieren um über bestimmte Ereignisse informiert zu werden die in Ihrem System auftreten.

Unterstützte Ereignisse:
- user.created
- user.updated  
- user.deleted

Die Webhook-URL können Sie in den Einstellungen konfigurieren.

## Best Practices

- Verwenden Sie immer HTTPS
- Speichern Sie API-Schlüssel sicher
- Implementieren Sie Retry-Logik
- Cachen Sie Antworten wo möglich




Weitere Informationen finden Sie im [Developer Portal](TODO).
