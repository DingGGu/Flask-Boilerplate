from datetime import timezone, timedelta

UTC = timezone.utc
KST = timezone(timedelta(hours=9), 'KST')
SGT = timezone(timedelta(hours=8), 'SGT')

tz_dict = dict(
    utc=UTC,
    kst=KST,
    sgt=SGT
)


def get_timezone(timezone_string: str) -> timezone:
    try:
        return tz_dict[timezone_string.lower()]
    except KeyError:
        raise RuntimeError('Unexpected timezone')
