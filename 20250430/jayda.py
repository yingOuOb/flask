@api.route("/add_point/<name>/<point>")
def add_point(name: str, point: int):
    """
    Add points to the team.
    
    Parameters
    ----------
    name: :type:`str`
        The name of the team.
        
    point: :type:`int`
        The point to add.
        
    Returns
    -------
    result: :type:`str`
        The status code.
        
    Status Codes
    ------------
    - S00000: Success
    - S00004: The team does not exist.
    - S99999: The game is not running.
    """
    
    if not is_admin():
        abort(403)
                
    if core.is_running is False:
        return STATUS_CODES.S99999
        
    if name not in core.teams:
        return STATUS_CODES.S00004
    
    return STATUS_CODES.S00000


# # function add_point() {
#     const team = document.getElementById("add_point_team_name").value;
#     const points = document.getElementById("add_points").value;

#     if (team === "" || points === "") {
#         alert("請填入隊伍名稱和分數");
#         return;
#     }

#     fetch(`/api/add_point/${team}/${points}`)
#         .then(response => response.text())
#         .then(response => { alert(response); });
# }