<center><p>Home Work 2</p>
<table border="1">
%for row in rows:
    <tr>
        <td>
            {{row[0]}}
        </td>
        <td>
            {{row[1]}}
        </td>
        <td>
{{row[2]}}
        </td>
        <td>
            <a href="/delete_item/{{row[0]}}"><i class="material-icons">delete</i></a>
        </td>
        <td>
            <a href="/update_item/{{row[0]}}"><i class="material-icons">Update</i></a>
        </td>
    </tr>
%end
</table>
</center>
<a href="/new_item">New Item...</a>